# SyndProxy validated proxy pool

## Current pool

- Alive now: 686
- Gold now: 464
- HTTP: 138 alive / 90 gold
- HTTPS: 146 alive / 37 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 230 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45875
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
