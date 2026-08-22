# SyndProxy private pool

## Current pool

- Alive now: 1015
- Gold now: 392
- HTTP: 321 alive / 82 gold
- HTTPS: 239 alive / 23 gold
- SOCKS4: 218 alive / 143 gold
- SOCKS5: 237 alive / 144 gold

## Historical pool

- Discovered: 165502
- Ever alive: 32279
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
