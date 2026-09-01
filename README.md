# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 462
- HTTP: 135 alive / 93 gold
- HTTPS: 120 alive / 31 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 186 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46674
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
