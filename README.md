# SyndProxy private pool

## Current pool

- Alive now: 827
- Gold now: 424
- HTTP: 234 alive / 94 gold
- HTTPS: 171 alive / 26 gold
- SOCKS4: 195 alive / 147 gold
- SOCKS5: 227 alive / 157 gold

## Historical pool

- Discovered: 162754
- Ever alive: 31570
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
