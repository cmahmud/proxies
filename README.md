# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 450
- HTTP: 100 alive / 77 gold
- HTTPS: 111 alive / 29 gold
- SOCKS4: 175 alive / 164 gold
- SOCKS5: 195 alive / 180 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47419
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
