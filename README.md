# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 381
- HTTP: 93 alive / 54 gold
- HTTPS: 38 alive / 10 gold
- SOCKS4: 172 alive / 154 gold
- SOCKS5: 188 alive / 163 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33427
- Ever gold: 1237

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
