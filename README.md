# SyndProxy private pool

## Current pool

- Alive now: 1055
- Gold now: 536
- HTTP: 386 alive / 165 gold
- HTTPS: 228 alive / 90 gold
- SOCKS4: 221 alive / 133 gold
- SOCKS5: 220 alive / 148 gold

## Historical pool

- Discovered: 123091
- Ever alive: 18732
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
