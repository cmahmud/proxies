# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 473
- HTTP: 154 alive / 96 gold
- HTTPS: 125 alive / 39 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 197 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45185
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
