# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 422
- HTTP: 154 alive / 75 gold
- HTTPS: 96 alive / 21 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33855
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
