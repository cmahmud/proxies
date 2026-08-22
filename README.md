# SyndProxy private pool

## Current pool

- Alive now: 928
- Gold now: 410
- HTTP: 304 alive / 93 gold
- HTTPS: 175 alive / 28 gold
- SOCKS4: 220 alive / 146 gold
- SOCKS5: 229 alive / 143 gold

## Historical pool

- Discovered: 163255
- Ever alive: 31767
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
