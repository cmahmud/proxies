# SyndProxy private pool

## Current pool

- Alive now: 832
- Gold now: 437
- HTTP: 220 alive / 92 gold
- HTTPS: 164 alive / 27 gold
- SOCKS4: 205 alive / 153 gold
- SOCKS5: 243 alive / 165 gold

## Historical pool

- Discovered: 162754
- Ever alive: 31570
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
