# SyndProxy validated proxy pool

## Current pool

- Alive now: 682
- Gold now: 465
- HTTP: 138 alive / 90 gold
- HTTPS: 140 alive / 37 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 231 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45883
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
