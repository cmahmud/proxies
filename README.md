# SyndProxy private pool

## Current pool

- Alive now: 659
- Gold now: 384
- HTTP: 164 alive / 63 gold
- HTTPS: 89 alive / 18 gold
- SOCKS4: 203 alive / 151 gold
- SOCKS5: 203 alive / 152 gold

## Historical pool

- Discovered: 146662
- Ever alive: 25726
- Ever gold: 1074

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
