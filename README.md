# SyndProxy private pool

## Current pool

- Alive now: 951
- Gold now: 353
- HTTP: 270 alive / 53 gold
- HTTPS: 199 alive / 15 gold
- SOCKS4: 243 alive / 147 gold
- SOCKS5: 239 alive / 138 gold

## Historical pool

- Discovered: 107085
- Ever alive: 14734
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
