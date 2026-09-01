# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 465
- HTTP: 146 alive / 94 gold
- HTTPS: 129 alive / 35 gold
- SOCKS4: 178 alive / 164 gold
- SOCKS5: 188 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46893
- Ever gold: 1456

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
