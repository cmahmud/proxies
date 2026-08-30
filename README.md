# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 424
- HTTP: 93 alive / 74 gold
- HTTPS: 64 alive / 25 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 191 alive / 164 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44430
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
