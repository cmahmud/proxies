# SyndProxy validated proxy pool

## Current pool

- Alive now: 656
- Gold now: 478
- HTTP: 147 alive / 98 gold
- HTTPS: 132 alive / 41 gold
- SOCKS4: 181 alive / 164 gold
- SOCKS5: 196 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46947
- Ever gold: 1458

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
