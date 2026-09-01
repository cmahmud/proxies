# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 454
- HTTP: 129 alive / 82 gold
- HTTPS: 132 alive / 34 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 194 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46748
- Ever gold: 1449

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
