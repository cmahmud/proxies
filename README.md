# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 384
- HTTP: 91 alive / 45 gold
- HTTPS: 49 alive / 13 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 180 alive / 165 gold

## Historical pool

- Discovered: 180671
- Ever alive: 33578
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
