# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 450
- HTTP: 126 alive / 84 gold
- HTTPS: 142 alive / 31 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46851
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
