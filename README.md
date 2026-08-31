# SyndProxy validated proxy pool

## Current pool

- Alive now: 681
- Gold now: 465
- HTTP: 142 alive / 95 gold
- HTTPS: 142 alive / 33 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 224 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46157
- Ever gold: 1441

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
