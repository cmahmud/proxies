# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 424
- HTTP: 93 alive / 65 gold
- HTTPS: 63 alive / 27 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 196 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45477
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
