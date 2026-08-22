# SyndProxy private pool

## Current pool

- Alive now: 879
- Gold now: 378
- HTTP: 268 alive / 71 gold
- HTTPS: 181 alive / 25 gold
- SOCKS4: 200 alive / 124 gold
- SOCKS5: 230 alive / 158 gold

## Historical pool

- Discovered: 164970
- Ever alive: 32250
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
