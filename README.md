# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 445
- HTTP: 116 alive / 88 gold
- HTTPS: 51 alive / 30 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 175 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49297
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
