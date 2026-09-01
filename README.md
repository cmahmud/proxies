# SyndProxy validated proxy pool

## Current pool

- Alive now: 609
- Gold now: 454
- HTTP: 133 alive / 88 gold
- HTTPS: 99 alive / 33 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 197 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46988
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
