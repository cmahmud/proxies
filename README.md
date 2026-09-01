# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 481
- HTTP: 134 alive / 97 gold
- HTTPS: 127 alive / 43 gold
- SOCKS4: 186 alive / 164 gold
- SOCKS5: 196 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46948
- Ever gold: 1458

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
