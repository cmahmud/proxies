# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 380
- HTTP: 94 alive / 53 gold
- HTTPS: 42 alive / 10 gold
- SOCKS4: 171 alive / 154 gold
- SOCKS5: 185 alive / 163 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33429
- Ever gold: 1237

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
