# SyndProxy private pool

## Current pool

- Alive now: 1040
- Gold now: 416
- HTTP: 359 alive / 92 gold
- HTTPS: 255 alive / 33 gold
- SOCKS4: 188 alive / 130 gold
- SOCKS5: 238 alive / 161 gold

## Historical pool

- Discovered: 161344
- Ever alive: 31124
- Ever gold: 1154

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
