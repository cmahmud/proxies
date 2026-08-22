# SyndProxy private pool

## Current pool

- Alive now: 775
- Gold now: 389
- HTTP: 198 alive / 82 gold
- HTTPS: 157 alive / 31 gold
- SOCKS4: 204 alive / 143 gold
- SOCKS5: 216 alive / 133 gold

## Historical pool

- Discovered: 163333
- Ever alive: 31900
- Ever gold: 1169

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
