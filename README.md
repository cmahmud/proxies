# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 473
- HTTP: 151 alive / 94 gold
- HTTPS: 128 alive / 41 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 197 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46940
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
