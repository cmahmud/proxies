# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 475
- HTTP: 145 alive / 96 gold
- HTTPS: 120 alive / 40 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 199 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46952
- Ever gold: 1458

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
