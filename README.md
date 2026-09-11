# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 435
- HTTP: 107 alive / 76 gold
- HTTPS: 54 alive / 25 gold
- SOCKS4: 183 alive / 164 gold
- SOCKS5: 184 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49134
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
