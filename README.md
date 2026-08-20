# SyndProxy private pool

## Current pool

- Alive now: 732
- Gold now: 387
- HTTP: 154 alive / 69 gold
- HTTPS: 138 alive / 16 gold
- SOCKS4: 226 alive / 147 gold
- SOCKS5: 214 alive / 155 gold

## Historical pool

- Discovered: 148155
- Ever alive: 26003
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
