# SyndProxy private pool

## Current pool

- Alive now: 1168
- Gold now: 555
- HTTP: 417 alive / 163 gold
- HTTPS: 288 alive / 95 gold
- SOCKS4: 236 alive / 150 gold
- SOCKS5: 227 alive / 147 gold

## Historical pool

- Discovered: 123176
- Ever alive: 18907
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
