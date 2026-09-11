# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 417
- HTTP: 87 alive / 66 gold
- HTTPS: 35 alive / 21 gold
- SOCKS4: 184 alive / 161 gold
- SOCKS5: 177 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48858
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
