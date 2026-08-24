# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 380
- HTTP: 104 alive / 55 gold
- HTTPS: 36 alive / 9 gold
- SOCKS4: 166 alive / 153 gold
- SOCKS5: 187 alive / 163 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33433
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
