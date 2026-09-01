# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 463
- HTTP: 135 alive / 93 gold
- HTTPS: 129 alive / 34 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 187 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46682
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
