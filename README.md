# SyndProxy private pool

## Current pool

- Alive now: 809
- Gold now: 416
- HTTP: 212 alive / 82 gold
- HTTPS: 153 alive / 29 gold
- SOCKS4: 206 alive / 147 gold
- SOCKS5: 238 alive / 158 gold

## Historical pool

- Discovered: 163333
- Ever alive: 31900
- Ever gold: 1169

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
