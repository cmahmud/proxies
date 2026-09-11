# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 444
- HTTP: 114 alive / 87 gold
- HTTPS: 47 alive / 28 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49246
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
