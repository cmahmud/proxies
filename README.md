# SyndProxy validated proxy pool

## Current pool

- Alive now: 584
- Gold now: 450
- HTTP: 97 alive / 77 gold
- HTTPS: 118 alive / 32 gold
- SOCKS4: 177 alive / 164 gold
- SOCKS5: 192 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47427
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
