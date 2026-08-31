# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 420
- HTTP: 97 alive / 65 gold
- HTTPS: 62 alive / 24 gold
- SOCKS4: 172 alive / 164 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45488
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
