# SyndProxy validated proxy pool

## Current pool

- Alive now: 609
- Gold now: 462
- HTTP: 138 alive / 88 gold
- HTTPS: 116 alive / 38 gold
- SOCKS4: 169 alive / 164 gold
- SOCKS5: 186 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46904
- Ever gold: 1456

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
