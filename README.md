# SyndProxy private pool

## Current pool

- Alive now: 957
- Gold now: 372
- HTTP: 313 alive / 91 gold
- HTTPS: 237 alive / 24 gold
- SOCKS4: 187 alive / 120 gold
- SOCKS5: 220 alive / 137 gold

## Historical pool

- Discovered: 153749
- Ever alive: 28838
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
