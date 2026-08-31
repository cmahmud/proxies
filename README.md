# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 422
- HTTP: 80 alive / 58 gold
- HTTPS: 71 alive / 32 gold
- SOCKS4: 186 alive / 161 gold
- SOCKS5: 189 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45498
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
