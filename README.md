# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 455
- HTTP: 137 alive / 86 gold
- HTTPS: 128 alive / 33 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 192 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46820
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
