# SyndProxy validated proxy pool

## Current pool

- Alive now: 665
- Gold now: 479
- HTTP: 156 alive / 99 gold
- HTTPS: 130 alive / 41 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 197 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46947
- Ever gold: 1458

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
