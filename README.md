# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 473
- HTTP: 130 alive / 92 gold
- HTTPS: 117 alive / 39 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 196 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46359
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
