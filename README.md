# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 451
- HTTP: 122 alive / 82 gold
- HTTPS: 128 alive / 32 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 196 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46746
- Ever gold: 1449

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
