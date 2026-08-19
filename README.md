# SyndProxy private pool

## Current pool

- Alive now: 1134
- Gold now: 538
- HTTP: 417 alive / 162 gold
- HTTPS: 282 alive / 92 gold
- SOCKS4: 207 alive / 140 gold
- SOCKS5: 228 alive / 144 gold

## Historical pool

- Discovered: 122378
- Ever alive: 18605
- Ever gold: 721

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
