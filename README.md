# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 437
- HTTP: 97 alive / 72 gold
- HTTPS: 104 alive / 30 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 192 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47339
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
