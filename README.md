# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 450
- HTTP: 127 alive / 94 gold
- HTTPS: 54 alive / 30 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49325
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
