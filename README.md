# SyndProxy validated proxy pool

## Current pool

- Alive now: 650
- Gold now: 477
- HTTP: 145 alive / 100 gold
- HTTPS: 129 alive / 38 gold
- SOCKS4: 183 alive / 163 gold
- SOCKS5: 193 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46946
- Ever gold: 1458

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
