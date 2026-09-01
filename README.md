# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 449
- HTTP: 125 alive / 84 gold
- HTTPS: 137 alive / 31 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 186 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46851
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
