# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 464
- HTTP: 126 alive / 91 gold
- HTTPS: 129 alive / 33 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 223 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45929
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
